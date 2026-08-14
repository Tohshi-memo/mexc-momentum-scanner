# Decision Report

- generated_at: 2026-08-14T00:16:21.166721+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11496**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11496, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.61% | **-1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.71% | **+0.77%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.07% | **+1.66%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.83% | **+1.55%** |
| MARKET_LONG | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.57% | **+1.29%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +2.28% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$601.25** / 初期 $100.00 (+501.25%)
- 確定: 3982件 (Win 1240 / Loss 1305 / Flat 1437) / skip 4075件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $601.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.94** / 初期 $100.00 (+49.94%)
- 確定: 1650件 (Win 471 / Loss 397 / Flat 782) / skip 3257件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0469 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $149.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.27** / 初期 $100.00 (+16.27%)
- 確定: 1469件 (Win 433 / Loss 556 / Flat 480) / pending 1件 / skip 1497件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000113 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AVAAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $116.27

## 6. Latest Market Context

- 更新: 2026-08-14T00:16:14.255402+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=63483.5
- Funnel: target 978 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +51.55% | $17,257,164.88 |
| US/USDT:USDT | +25.30% | $5,613,863.58 |
| WDAYSTOCK/USDT:USDT | +17.14% | $1,207,172.20 |
| PROM/USDT:USDT | +15.85% | $2,637,775.12 |
| BLESS/USDT:USDT | +14.15% | $9,732,625.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOS/USDT:USDT | below_1h_threshold | +2.86% | +2.82% |
| US/USDT:USDT | below_1h_threshold | +2.86% | +2.82% |
| ON/USDT:USDT | below_1h_threshold | +2.62% | +2.58% |
| ACE/USDT:USDT | below_1h_threshold | +1.48% | +1.43% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.21% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
