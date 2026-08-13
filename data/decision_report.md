# Decision Report

- generated_at: 2026-08-13T22:21:23.905893+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11486**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11486, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.43% | **+0.19%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.06% | **+1.13%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.49% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.15% | **+0.86%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$601.25** / 初期 $100.00 (+501.25%)
- 確定: 3981件 (Win 1240 / Loss 1305 / Flat 1436) / skip 4066件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.35% 残高後 $601.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.94** / 初期 $100.00 (+49.94%)
- 確定: 1650件 (Win 471 / Loss 397 / Flat 782) / skip 3247件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0045 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $149.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.27** / 初期 $100.00 (+16.27%)
- 確定: 1469件 (Win 433 / Loss 556 / Flat 480) / pending 1件 / skip 1492件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000085 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AVAAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $116.27

## 6. Latest Market Context

- 更新: 2026-08-13T22:21:15.785124+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=63543.0
- Funnel: target 978 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +43.89% | $10,397,020.28 |
| US/USDT:USDT | +20.24% | $5,403,597.78 |
| CATE/USDT:USDT | +17.92% | $1,379,194.88 |
| WDAYSTOCK/USDT:USDT | +17.50% | $1,103,910.04 |
| H/USDT:USDT | +10.61% | $1,357,487.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +3.09% | +2.93% |
| AVAAI/USDT:USDT | below_1h_threshold | +2.15% | +2.00% |
| PROM/USDT:USDT | below_1h_threshold | +1.85% | +1.69% |
| ON/USDT:USDT | below_1h_threshold | +1.30% | +1.15% |
| ACE/USDT:USDT | below_1h_threshold | +1.00% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
