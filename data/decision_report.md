# Decision Report

- generated_at: 2026-07-02T20:55:55.668917+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8107**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8107, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +2.30% | **+0.35%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_BB3S | 4/16 | 25.0% | +0.32% | **+0.08%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.12% | **+0.04%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.01% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.70% | **+1.80%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.19% | **+1.75%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.85% | **+1.35%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.63% | **+0.98%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.17% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$103.14** / 初期 $100.00 (+3.14%)
- 確定トレード: 52件 (TP 19 / SL 32 / EXP 1)
- 最新: TAIKO/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2224件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.86** / 初期 $100.00 (+5.86%)
- 確定: 566件 (Win 137 / Loss 131 / Flat 298) / skip 952件
- 成長率目線: 平均log +0.000101 / 幾何平均 +0.010% per trade / maxDD +3.53%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0551 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MERL/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $105.86

## 5. Latest Market Context

- 更新: 2026-07-02T20:55:42.032215+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=61405.4
- Funnel: target 834 → liquid 173 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +16.91% | $4,563,729.65 |
| PIPPIN/USDT:USDT | +15.39% | $3,449,073.73 |
| BASED/USDT:USDT | +13.75% | $14,577,577.64 |
| TAIKO/USDT:USDT | +13.64% | $101,726,642.39 |
| LAB/USDT:USDT | +12.65% | $11,634,507.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.66% | +4.73% |
| RAVE/USDT:USDT | below_1h_threshold | +2.26% | +2.34% |
| BSB/USDT:USDT | below_1h_threshold | +1.33% | +1.40% |
| EVAA/USDT:USDT | below_1h_threshold | +1.30% | +1.38% |
| BILL/USDT:USDT | below_1h_threshold | +1.25% | +1.33% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
