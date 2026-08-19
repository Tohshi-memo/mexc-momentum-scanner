# Decision Report

- generated_at: 2026-08-19T03:46:36.515405+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11947**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11947, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_7PCT | 7/20 | 35.0% | +3.09% | **+1.08%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.77% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.33% | **+1.00%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.09% | **+0.76%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.06% | **+0.76%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.51** / 初期 $100.00 (+514.51%)
- 確定: 4211件 (Win 1295 / Loss 1375 / Flat 1541) / skip 4297件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $614.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3537件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0349 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.70** / 初期 $100.00 (+17.70%)
- 確定: 1727件 (Win 516 / Loss 659 / Flat 552) / pending 2件 / skip 1689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000187 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $117.70

## 6. Latest Market Context

- 更新: 2026-08-19T03:46:25.276080+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64307.5
- Funnel: target 992 → liquid 178 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +38.29% | $36,597,196.84 |
| UNITREE/USDT:USDT | +28.89% | $8,854,933.65 |
| TRIA/USDT:USDT | +25.21% | $5,133,109.50 |
| NIULAI/USDT:USDT | +13.77% | $5,725,235.94 |
| US/USDT:USDT | +7.51% | $1,106,968.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRIA/USDT:USDT | below_1h_threshold | +3.42% | +3.44% |
| SKDD/USDT:USDT | below_1h_threshold | +1.78% | +1.80% |
| SOXS/USDT:USDT | below_1h_threshold | +1.58% | +1.60% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.50% | +1.52% |
| LINK/USDT:USDT | below_1h_threshold | +1.35% | +1.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
