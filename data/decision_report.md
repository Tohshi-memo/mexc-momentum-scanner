# Decision Report

- generated_at: 2026-07-04T12:09:36.156622+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8258**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8258, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +2.01% | **+0.50%** |
| LIMIT_7PCT | 2/20 | 10.0% | +3.10% | **+0.31%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.08% | **+0.22%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.47% | **+0.21%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.47% | **-0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.61% | **+1.61%** |
| MARKET_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.08% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$331.94** / 初期 $100.00 (+231.94%)
- 確定: 2575件 (Win 813 / Loss 858 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000466 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OGN/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $331.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1032件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0437 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T12:09:26.460334+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=62524.6
- Funnel: target 834 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +100.42% | $66,004,726.12 |
| HMSTR/USDT:USDT | +85.33% | $10,437,702.19 |
| TLM/USDT:USDT | +85.25% | $51,843,382.73 |
| ANSEM/USDT:USDT | +83.80% | $5,671,804.02 |
| VELVET/USDT:USDT | +46.12% | $34,664,949.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OGN/USDT:USDT | below_1h_threshold | +4.40% | +4.29% |
| BEAT/USDT:USDT | below_1h_threshold | +3.36% | +3.26% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.25% | +3.14% |
| EPIC/USDT:USDT | below_1h_threshold | +2.72% | +2.62% |
| VELVET/USDT:USDT | below_1h_threshold | +2.17% | +2.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
