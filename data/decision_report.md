# Decision Report

- generated_at: 2026-08-10T03:21:19.267933+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11115**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.70% / filled 20/20。**
- 全期間 MARKET基準: n=11115, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.42% | **+2.30%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.12% | **+1.80%** |
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_BB3S | 2/15 | 13.3% | +4.30% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +2.23% | **+2.23%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +3.19% | **+2.23%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +2.96% | **+1.77%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.56% | **+0.45%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.07% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$624.97** / 初期 $100.00 (+524.97%)
- 確定: 3933件 (Win 1230 / Loss 1282 / Flat 1421) / skip 3743件
- 成長率目線: 平均log +0.000466 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $624.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3013件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.30** / 初期 $100.00 (+17.30%)
- 確定: 1283件 (Win 397 / Loss 493 / Flat 393) / pending 0件 / skip 1303件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` EXPIRED account +0.20% 残高後 $117.30

## 6. Latest Market Context

- 更新: 2026-08-10T03:21:11.092618+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=65034.0
- Funnel: target 961 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +55.16% | $82,185,289.03 |
| BMT/USDT:USDT | +48.28% | $19,062,159.62 |
| CAP/USDT:USDT | +24.94% | $2,665,329.94 |
| TST/USDT:USDT | +16.41% | $2,965,197.00 |
| NIL/USDT:USDT | +13.61% | $2,321,517.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +3.50% | +3.56% |
| PEOPLE/USDT:USDT | below_1h_threshold | +3.06% | +3.13% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.80% | +2.87% |
| COAI/USDT:USDT | below_1h_threshold | +2.00% | +2.07% |
| CASHCAT/USDT:USDT | below_1h_threshold | +1.84% | +1.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
