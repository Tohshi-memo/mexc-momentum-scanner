# Decision Report

- generated_at: 2026-10-21T05:51:27.078976+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17097**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=17097, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.04% | **+1.94%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.00% | **+1.40%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.55% | **+1.24%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.86% | **+1.21%** |
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +3.77% | **+3.77%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.49% | **+1.37%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.60% | **+0.96%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.06% | **+0.93%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 249件 (TP 92 / SL 150 / EXP 7)
- 最新: ICNT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,352.02** / 初期 $100.00 (+1252.02%)
- 確定: 6489件 (Win 1890 / Loss 2071 / Flat 2528) / skip 7169件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SMCISTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.60% 残高後 $1,352.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$280.59** / 初期 $100.00 (+180.59%)
- 確定: 3819件 (Win 1051 / Loss 892 / Flat 1876) / skip 6689件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0361 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.18% 残高後 $280.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5255件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000256 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-21T05:51:11.963188+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=82733.4
- Funnel: target 1084 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOOD/USDT:USDT | +40.00% | $2,686,382.38 |
| IOST/USDT:USDT | +33.77% | $2,423,830.71 |
| ICNT/USDT:USDT | +31.12% | $4,538,309.40 |
| BIRB/USDT:USDT | +28.40% | $1,037,412.92 |
| CVX/USDT:USDT | +19.05% | $1,252,424.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOOD/USDT:USDT | below_1h_threshold | +4.32% | +4.37% |
| CHIP/USDT:USDT | below_1h_threshold | +3.35% | +3.41% |
| ICNT/USDT:USDT | below_1h_threshold | +1.65% | +1.70% |
| SYRUP/USDT:USDT | below_1h_threshold | +1.10% | +1.15% |
| GRASS/USDT:USDT | below_1h_threshold | +0.93% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
