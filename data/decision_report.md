# Decision Report

- generated_at: 2026-11-13T15:06:30.627411+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18825**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18825, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +6.86% | **+2.06%** |
| LIMIT_10PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_8PCT | 7/20 | 35.0% | +4.44% | **+1.56%** |
| LIMIT_7PCT | 8/20 | 40.0% | +1.75% | **+0.70%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.53% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.26% | **+2.12%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.95% | **+1.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.15% | **+1.18%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,763.10** / 初期 $100.00 (+1663.10%)
- 確定: 7289件 (Win 2100 / Loss 2337 / Flat 2852) / skip 8097件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BARD/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,763.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$396.05** / 初期 $100.00 (+296.05%)
- 確定: 4833件 (Win 1300 / Loss 1077 / Flat 2456) / skip 7403件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1331 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KGEN/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $396.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6985件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000293 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T15:06:14.903682+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=68906.5
- Funnel: target 1084 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +138.32% | $31,025,105.19 |
| BARD/USDT:USDT | +88.40% | $23,475,292.71 |
| SOPH/USDT:USDT | +36.71% | $1,025,145.32 |
| KOR/USDT:USDT | +26.06% | $1,912,240.38 |
| ARIA/USDT:USDT | +18.84% | $9,966,315.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SQQQ/USDT:USDT | below_1h_threshold | +3.52% | +3.64% |
| BARD/USDT:USDT | below_1h_threshold | +2.31% | +2.42% |
| METASTOCK/USDT:USDT | below_1h_threshold | +1.46% | +1.58% |
| UAI/USDT:USDT | below_1h_threshold | +0.70% | +0.81% |
| KOR/USDT:USDT | below_1h_threshold | +0.48% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
