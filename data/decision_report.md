# Decision Report

- generated_at: 2026-06-28T00:51:49.305030+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7722**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7722, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +5.46% | **+1.09%** |
| LIMIT_BB3S | 4/13 | 30.8% | +0.12% | **+0.04%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_5PCT | 6/20 | 30.0% | -1.52% | **-0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| ASK_LONG | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_BB3S_LONG | 2/7 | 28.6% | +0.35% | **+0.10%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.13% | **+0.09%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.08% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$238.34** / 初期 $100.00 (+138.34%)
- 確定: 2230件 (Win 670 / Loss 745 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $238.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.83** / 初期 $100.00 (+6.83%)
- 確定: 453件 (Win 120 / Loss 118 / Flat 215) / skip 680件
- 成長率目線: 平均log +0.000146 / 幾何平均 +0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0087 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.83

## 5. Latest Market Context

- 更新: 2026-06-28T00:51:41.418496+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=60126.1
- Funnel: target 806 → liquid 120 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BAS/USDT:USDT | +17.26% | $2,536,376.09 |
| LAB/USDT:USDT | +14.20% | $42,892,436.46 |
| SLX/USDT:USDT | +9.45% | $19,148,028.48 |
| S/USDT:USDT | +8.66% | $4,551,327.66 |
| SIREN/USDT:USDT | +7.46% | $1,196,984.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +3.95% | +3.74% |
| LAB/USDT:USDT | below_1h_threshold | +3.79% | +3.58% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.15% | +2.94% |
| BEAT/USDT:USDT | below_1h_threshold | +3.07% | +2.86% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.70% | +2.49% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
