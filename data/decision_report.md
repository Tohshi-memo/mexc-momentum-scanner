# Decision Report

- generated_at: 2026-06-28T00:17:50.076338+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7719**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7719, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.76% | **-0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +5.46% | **+1.09%** |
| LIMIT_BB3S | 4/12 | 33.3% | +0.12% | **+0.04%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_5PCT | 6/20 | 30.0% | -1.52% | **-0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.56% | **+1.56%** |
| ASK_LONG | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.53% | **+0.29%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +0.40% | **+0.24%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.31% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$238.34** / 初期 $100.00 (+138.34%)
- 確定: 2228件 (Win 669 / Loss 744 / Flat 815) / skip 2052件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $238.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.58** / 初期 $100.00 (+7.58%)
- 確定: 450件 (Win 120 / Loss 116 / Flat 214) / skip 680件
- 成長率目線: 平均log +0.000162 / 幾何平均 +0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0339 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $107.58

## 5. Latest Market Context

- 更新: 2026-06-28T00:17:45.494862+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=60124.9
- Funnel: target 806 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BAS/USDT:USDT | +16.57% | $2,387,392.28 |
| LAB/USDT:USDT | +13.16% | $42,229,945.25 |
| SLX/USDT:USDT | +12.82% | $18,959,082.60 |
| SNX/USDT:USDT | +8.42% | $1,238,644.45 |
| VELVET/USDT:USDT | +8.18% | $247,346,497.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_relative_strength | +5.11% | +4.90% |
| M/USDT:USDT | below_1h_threshold | +3.96% | +3.75% |
| SLX/USDT:USDT | below_1h_threshold | +3.40% | +3.19% |
| BAS/USDT:USDT | below_1h_threshold | +3.18% | +2.97% |
| BEAT/USDT:USDT | below_1h_threshold | +2.92% | +2.71% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
