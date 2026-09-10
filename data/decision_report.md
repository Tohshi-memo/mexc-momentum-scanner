# Decision Report

- generated_at: 2026-09-10T02:56:29.506420+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14147**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14147, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +3.42% | **+1.37%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.89% | **+1.13%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +4.62% | **+3.93%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +5.17% | **+3.36%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.81% | **+2.67%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +4.23% | **+1.69%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,064.11** / 初期 $100.00 (+964.11%)
- 確定: 5327件 (Win 1603 / Loss 1717 / Flat 2007) / skip 5381件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,064.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.20** / 初期 $100.00 (+108.20%)
- 確定: 2741件 (Win 759 / Loss 641 / Flat 1341) / skip 4817件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0894 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $208.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.36** / 初期 $100.00 (+22.36%)
- 確定: 2652件 (Win 783 / Loss 1011 / Flat 858) / pending 5件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000572 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.36

## 6. Latest Market Context

- 更新: 2026-09-10T02:56:14.702621+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=78324.7
- Funnel: target 1064 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.8 >= 65=1, 4h RSI 88.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +53.46% | $1,819,861.81 |
| CATE/USDT:USDT | +35.23% | $2,926,686.23 |
| BTR/USDT:USDT | +25.81% | $2,612,716.46 |
| VET/USDT:USDT | +3.44% | $7,738,513.72 |
| KAS/USDT:USDT | +2.69% | $4,126,257.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ATOM/USDT:USDT | below_1h_threshold | +3.61% | +3.28% |
| AERO/USDT:USDT | below_1h_threshold | +2.50% | +2.16% |
| VET/USDT:USDT | below_1h_threshold | +2.47% | +2.14% |
| INJ/USDT:USDT | below_1h_threshold | +2.16% | +1.82% |
| MINA/USDT:USDT | below_1h_threshold | +1.60% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
