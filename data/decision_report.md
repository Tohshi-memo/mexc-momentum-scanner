# Decision Report

- generated_at: 2026-06-28T10:02:02.259958+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7737**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7737, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.09% | **-0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.08% | **-0.02%** |
| ASK | 20/20 | 100.0% | -0.04% | **-0.04%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |
| MARKET | 20/20 | 100.0% | -0.09% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.48% | **+0.25%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$245.54** / 初期 $100.00 (+145.54%)
- 確定: 2245件 (Win 680 / Loss 750 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $245.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 693件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T10:01:57.556066+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=60244.0
- Funnel: target 805 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +34.71% | $10,171,568.88 |
| S/USDT:USDT | +22.93% | $6,898,154.82 |
| SIREN/USDT:USDT | +20.71% | $1,569,698.67 |
| LAB/USDT:USDT | +17.39% | $35,269,257.74 |
| BASED/USDT:USDT | +16.88% | $1,765,201.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| S/USDT:USDT | below_1h_threshold | +0.80% | +0.78% |
| ALLO/USDT:USDT | below_1h_threshold | +0.71% | +0.69% |
| VELVET/USDT:USDT | below_1h_threshold | +0.65% | +0.63% |
| SIREN/USDT:USDT | below_1h_threshold | +0.62% | +0.60% |
| LIT/USDT:USDT | below_1h_threshold | +0.29% | +0.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
