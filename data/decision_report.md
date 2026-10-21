# Decision Report

- generated_at: 2026-10-21T01:31:24.014059+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17085**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.46% / filled 20/20。**
- 全期間 MARKET基準: n=17085, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.46% | **+1.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.03% | **+1.93%** |
| LIMIT_ATR | 15/20 | 75.0% | +2.35% | **+1.76%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.54% | **+1.65%** |
| MARKET | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.62% | **+1.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.07% | **+0.59%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.36% | **+0.16%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.80% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 248件 (TP 92 / SL 149 / EXP 7)
- 最新: USELESS/USDT:USDT TP_HIT PnL +7.06% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,344.00** / 初期 $100.00 (+1244.00%)
- 確定: 6488件 (Win 1889 / Loss 2071 / Flat 2528) / skip 7158件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AERO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.84% 残高後 $1,344.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$280.10** / 初期 $100.00 (+180.10%)
- 確定: 3818件 (Win 1050 / Loss 892 / Flat 1876) / skip 6678件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0084 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $280.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5246件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000225 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-21T01:31:11.625250+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=82931.0
- Funnel: target 1084 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ICNT/USDT:USDT | +18.81% | $3,791,235.87 |
| DOOD/USDT:USDT | +18.58% | $1,876,262.72 |
| SMCISTOCK/USDT:USDT | +16.82% | $1,296,398.89 |
| BTW/USDT:USDT | +11.05% | $27,106,696.72 |
| SPCXSTOCK/USDT:USDT | +8.59% | $88,768,623.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BATON/USDT:USDT | below_1h_threshold | +2.69% | +2.76% |
| INJ/USDT:USDT | below_1h_threshold | +2.67% | +2.75% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.38% | +2.45% |
| MUU/USDT:USDT | below_1h_threshold | +1.78% | +1.85% |
| AKE/USDT:USDT | below_1h_threshold | +1.66% | +1.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
