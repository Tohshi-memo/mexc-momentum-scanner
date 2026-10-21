# Decision Report

- generated_at: 2026-10-21T00:56:37.884718+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17083**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.65% / filled 20/20。**
- 全期間 MARKET基準: n=17083, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.65% | **+1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.70% | **+1.53%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.94% | **+1.36%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.09% | **+1.25%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.13% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.76% | **+0.08%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.04% | **+0.03%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 248件 (TP 92 / SL 149 / EXP 7)
- 最新: USELESS/USDT:USDT TP_HIT PnL +7.06% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,344.00** / 初期 $100.00 (+1244.00%)
- 確定: 6488件 (Win 1889 / Loss 2071 / Flat 2528) / skip 7156件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AERO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.84% 残高後 $1,344.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$280.10** / 初期 $100.00 (+180.10%)
- 確定: 3818件 (Win 1050 / Loss 892 / Flat 1876) / skip 6676件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0084 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $280.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5246件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-21T00:56:20.101098+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=83062.7
- Funnel: target 1084 → liquid 168 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOOD/USDT:USDT | +21.14% | $1,792,895.77 |
| ICNT/USDT:USDT | +20.53% | $3,751,660.32 |
| SMCISTOCK/USDT:USDT | +16.88% | $1,281,593.17 |
| BTW/USDT:USDT | +11.09% | $27,495,102.35 |
| SPCXSTOCK/USDT:USDT | +8.85% | $88,392,644.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_1h_threshold | +3.06% | +2.97% |
| VVV/USDT:USDT | below_1h_threshold | +2.97% | +2.88% |
| USELESS/USDT:USDT | below_1h_threshold | +2.92% | +2.82% |
| PONS/USDT:USDT | below_1h_threshold | +2.81% | +2.72% |
| ZEC/USDT:USDT | below_1h_threshold | +2.25% | +2.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
