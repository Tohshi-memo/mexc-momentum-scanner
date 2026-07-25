# Decision Report

- generated_at: 2026-07-25T05:46:23.166596+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9484**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=9484, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_BB3S | 4/20 | 20.0% | +1.11% | **+0.22%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.97% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.36% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.47% | **+0.81%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.97% | **+0.73%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.92% | **+0.55%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.74% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 139件 (TP 46 / SL 88 / EXP 5)
- 最新: SYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$423.36** / 初期 $100.00 (+323.36%)
- 確定: 3326件 (Win 1048 / Loss 1077 / Flat 1201) / skip 2719件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $423.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1730件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0841 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$104.60** / 初期 $100.00 (+4.60%)
- 確定: 535件 (Win 178 / Loss 209 / Flat 148) / pending 5件 / skip 416件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000251 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $104.60

## 6. Latest Market Context

- 更新: 2026-07-25T05:46:13.062028+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=64009.0
- Funnel: target 898 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +65.82% | $60,696,399.78 |
| EUL/USDT:USDT | +21.24% | $1,317,805.97 |
| B2/USDT:USDT | +19.91% | $2,704,248.47 |
| ZAMA/USDT:USDT | +16.47% | $3,901,458.39 |
| PROM/USDT:USDT | +16.18% | $2,598,852.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +2.70% | +2.91% |
| BANK/USDT:USDT | below_1h_threshold | +2.66% | +2.88% |
| EUL/USDT:USDT | below_1h_threshold | +2.39% | +2.60% |
| VELVET/USDT:USDT | below_1h_threshold | +2.14% | +2.36% |
| EVAA/USDT:USDT | below_1h_threshold | +1.77% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
