# Decision Report

- generated_at: 2026-11-22T02:56:26.648009+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19355**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19355, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +2.29% | **+1.60%** |
| LIMIT_BB3S | 11/17 | 64.7% | +2.24% | **+1.45%** |
| LIMIT_5PCT | 10/20 | 50.0% | +2.78% | **+1.39%** |
| LIMIT_6PCT | 8/20 | 40.0% | +2.71% | **+1.08%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +4.56% | **+1.83%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.13% | **+1.72%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.76% | **+1.67%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +5.33% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,786.94** / 初期 $100.00 (+1686.94%)
- 確定: 7480件 (Win 2149 / Loss 2407 / Flat 2924) / skip 8436件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.68% 残高後 $1,786.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$448.22** / 初期 $100.00 (+348.22%)
- 確定: 5124件 (Win 1363 / Loss 1100 / Flat 2661) / skip 7642件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1169 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $448.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7515件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000395 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T02:56:16.744449+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.91% price=59544.2
- Funnel: target 1086 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +31.20% | $2,099,383.03 |
| DCTY/USDT:USDT | +23.70% | $1,594,020.53 |
| BTW/USDT:USDT | +13.34% | $5,684,615.76 |
| PIEVERSE/USDT:USDT | +13.21% | $5,886,394.81 |
| SKYAI/USDT:USDT | +10.61% | $1,430,571.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLAUDIA/USDT:USDT | below_1h_threshold | +3.68% | +4.59% |
| IRYS/USDT:USDT | below_1h_threshold | +0.59% | +1.49% |
| SPX/USDT:USDT | below_1h_threshold | +0.50% | +1.41% |
| KORU/USDT:USDT | below_1h_threshold | +0.39% | +1.30% |
| MUU/USDT:USDT | below_1h_threshold | +0.29% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
