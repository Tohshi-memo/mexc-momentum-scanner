# Decision Report

- generated_at: 2026-08-21T18:26:27.247763+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12235**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12235, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.65% | **+0.62%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +4.42% | **+1.99%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +3.36% | **+1.85%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.28% | **+1.82%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.50% | **+1.75%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.52** / 初期 $100.00 (+543.52%)
- 確定: 4364件 (Win 1338 / Loss 1435 / Flat 1591) / skip 4432件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $643.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.56** / 初期 $100.00 (+56.56%)
- 確定: 1846件 (Win 512 / Loss 439 / Flat 895) / skip 3800件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0899 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $156.56

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1890件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000279 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T18:26:16.857342+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77407.8
- Funnel: target 1018 → liquid 212 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +33.03% | $11,013,219.03 |
| JIMOTHY/USDT:USDT | +16.74% | $1,092,809.64 |
| BLESS/USDT:USDT | +13.68% | $7,186,483.23 |
| BEAT/USDT:USDT | +12.46% | $55,188,754.66 |
| PEPE/USDT:USDT | +10.16% | $395,991,425.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GPS/USDT:USDT | below_1h_threshold | +3.08% | +3.05% |
| FLOKI/USDT:USDT | below_1h_threshold | +2.82% | +2.78% |
| ZORA/USDT:USDT | below_1h_threshold | +2.79% | +2.75% |
| EVAA/USDT:USDT | below_1h_threshold | +2.65% | +2.61% |
| ALIGN/USDT:USDT | below_1h_threshold | +2.59% | +2.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
