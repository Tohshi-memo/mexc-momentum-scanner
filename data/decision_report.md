# Decision Report

- generated_at: 2026-08-14T23:26:20.756952+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11618**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11618, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.48% | **+0.99%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.56% | **+0.42%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.42% | **+0.40%** |
| LIMIT_BB3S | 2/17 | 11.8% | +2.00% | **+0.24%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.25% | **+0.94%** |
| MARKET_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.75% | **+0.64%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.78** / 初期 $100.00 (+540.78%)
- 確定: 4086件 (Win 1281 / Loss 1345 / Flat 1460) / skip 4093件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $640.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$153.05** / 初期 $100.00 (+53.05%)
- 確定: 1681件 (Win 482 / Loss 407 / Flat 792) / skip 3348件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0709 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $153.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.73** / 初期 $100.00 (+17.73%)
- 確定: 1566件 (Win 477 / Loss 600 / Flat 489) / pending 0件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000263 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.73

## 6. Latest Market Context

- 更新: 2026-08-14T23:26:12.318241+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=62917.7
- Funnel: target 985 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +23.33% | $6,744,775.75 |
| ACE/USDT:USDT | +19.65% | $76,019,845.18 |
| DOLO/USDT:USDT | +13.69% | $1,648,612.91 |
| HEI/USDT:USDT | +12.88% | $5,667,792.74 |
| ONE/USDT:USDT | +11.80% | $1,044,196.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +2.86% | +2.76% |
| AEON1/USDT:USDT | below_1h_threshold | +2.15% | +2.06% |
| US/USDT:USDT | below_1h_threshold | +1.78% | +1.68% |
| CYS/USDT:USDT | below_1h_threshold | +1.76% | +1.66% |
| JTO/USDT:USDT | below_1h_threshold | +1.45% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
