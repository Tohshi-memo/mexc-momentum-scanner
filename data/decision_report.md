# Decision Report

- generated_at: 2026-11-21T17:31:30.457444+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19325**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19325, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +1.47% | **+1.40%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.94% | **+0.89%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +4.60% | **+1.84%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.29% | **+1.48%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.15% | **+1.45%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.85% | **+1.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,727.37** / 初期 $100.00 (+1627.37%)
- 確定: 7468件 (Win 2143 / Loss 2402 / Flat 2923) / skip 8418件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,727.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$448.22** / 初期 $100.00 (+348.22%)
- 確定: 5124件 (Win 1363 / Loss 1100 / Flat 2661) / skip 7612件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0238 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $448.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7487件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000194 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T17:31:16.438442+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=60113.4
- Funnel: target 1086 → liquid 138 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +30.98% | $1,679,737.00 |
| PIEVERSE/USDT:USDT | +12.84% | $4,664,755.21 |
| DODO/USDT:USDT | +5.98% | $1,487,743.97 |
| IDOL/USDT:USDT | +5.91% | $1,885,100.13 |
| NIGHT/USDT:USDT | +5.86% | $1,113,088.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIGHT/USDT:USDT | below_1h_threshold | +4.33% | +4.19% |
| IDOL/USDT:USDT | below_1h_threshold | +2.16% | +2.03% |
| MMT/USDT:USDT | below_1h_threshold | +2.07% | +1.93% |
| LUNC/USDT:USDT | below_1h_threshold | +2.05% | +1.91% |
| EVAA/USDT:USDT | below_1h_threshold | +1.87% | +1.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
