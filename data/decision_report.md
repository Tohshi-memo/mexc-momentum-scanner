# Decision Report

- generated_at: 2026-07-04T16:13:46.298470+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8273**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8273, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.03% | **+0.41%** |
| LIMIT_6PCT | 3/20 | 15.0% | +2.09% | **+0.31%** |
| LIMIT_7PCT | 2/20 | 10.0% | +3.10% | **+0.31%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.02% | **+0.31%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.24% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.55% | **+0.93%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.81% | **+0.65%** |
| MARKET_LONG | 20/20 | 100.0% | +0.54% | **+0.54%** |
| ASK_LONG | 20/20 | 100.0% | +0.50% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$330.22** / 初期 $100.00 (+230.22%)
- 確定: 2590件 (Win 820 / Loss 866 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000461 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $330.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1047件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T16:13:36.200985+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=62780.5
- Funnel: target 834 → liquid 152 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VANRY/USDT:USDT | +6.29% | $1,720,076.36 |
| SKYAI/USDT:USDT | +5.12% | $9,013,534.14 |
| RAVE/USDT:USDT | +5.11% | $3,216,532.19 |
| MAGMA/USDT:USDT | +4.67% | $16,776,521.26 |
| HMSTR/USDT:USDT | +3.75% | $15,095,704.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.52% | +4.72% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.85% | +4.05% |
| TLM/USDT:USDT | below_1h_threshold | +3.60% | +3.80% |
| CAP/USDT:USDT | below_1h_threshold | +2.64% | +2.85% |
| EPIC/USDT:USDT | below_1h_threshold | +2.56% | +2.77% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
