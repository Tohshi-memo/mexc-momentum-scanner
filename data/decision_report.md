# Decision Report

- generated_at: 2026-10-17T17:56:32.946527+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16911**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16911, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.98% | **+0.69%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +5.11% | **+5.11%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.57% | **+1.93%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.80% | **+1.68%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.84% | **+1.57%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.27% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,295.62** / 初期 $100.00 (+1195.62%)
- 確定: 6384件 (Win 1861 / Loss 2040 / Flat 2483) / skip 7088件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,295.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3690件 (Win 1027 / Loss 878 / Flat 1785) / skip 6632件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0571 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5075件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000270 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-17T17:56:17.639149+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=81342.1
- Funnel: target 1084 → liquid 150 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.0 >= 65=1, 4h RSI 74.0 >= 65=1, 4h RSI 97.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +18.76% | $5,724,209.17 |
| AVA/USDT:USDT | +14.40% | $1,303,727.29 |
| ICNT/USDT:USDT | +14.25% | $12,796,736.53 |
| AGT/USDT:USDT | +13.65% | $21,288,221.90 |
| BTW/USDT:USDT | +12.66% | $28,128,800.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +4.68% | +4.54% |
| BR/USDT:USDT | below_1h_threshold | +3.95% | +3.81% |
| SIREN/USDT:USDT | below_1h_threshold | +3.29% | +3.15% |
| LSK/USDT:USDT | below_1h_threshold | +2.78% | +2.64% |
| MAGIC/USDT:USDT | below_1h_threshold | +2.51% | +2.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
