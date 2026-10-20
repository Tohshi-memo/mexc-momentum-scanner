# Decision Report

- generated_at: 2026-10-20T12:41:21.185535+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17063**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17063, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.17% | **-1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 10/10 | 100.0% | +3.41% | **+3.41%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.02% | **+1.97%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.42% | **+1.94%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.36% | **+1.41%** |
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 247件 (TP 91 / SL 149 / EXP 7)
- 最新: BAT/USDT:USDT SL_HIT PnL -3.97% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,344.26** / 初期 $100.00 (+1244.26%)
- 確定: 6483件 (Win 1887 / Loss 2068 / Flat 2528) / skip 7141件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $1,344.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$285.05** / 初期 $100.00 (+185.05%)
- 確定: 3811件 (Win 1050 / Loss 887 / Flat 1874) / skip 6663件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0877 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $285.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5222件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000417 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T12:41:08.441227+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=81532.6
- Funnel: target 1083 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +121.66% | $15,076,735.26 |
| APR/USDT:USDT | +32.60% | $1,182,179.44 |
| ALT/USDT:USDT | +21.93% | $2,340,128.57 |
| PHA/USDT:USDT | +16.00% | $19,888,279.96 |
| A/USDT:USDT | +13.61% | $23,239,060.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.10% | +4.02% |
| A/USDT:USDT | below_1h_threshold | +2.57% | +2.49% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.78% | +1.70% |
| S/USDT:USDT | below_1h_threshold | +1.56% | +1.48% |
| KAS/USDT:USDT | below_1h_threshold | +1.53% | +1.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
