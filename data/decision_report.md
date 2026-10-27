# Decision Report

- generated_at: 2026-10-27T15:46:31.054425+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17613**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17613, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.75% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.39% | **+1.92%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +4.33% | **+1.30%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 254件 (TP 94 / SL 152 / EXP 8)
- 最新: APR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,546.26** / 初期 $100.00 (+1446.26%)
- 確定: 6725件 (Win 1958 / Loss 2152 / Flat 2615) / skip 7449件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,546.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$340.03** / 初期 $100.00 (+240.03%)
- 確定: 4142件 (Win 1133 / Loss 960 / Flat 2049) / skip 6882件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1199 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $340.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5775件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000291 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T15:46:15.291840+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=80626.0
- Funnel: target 1083 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +231.65% | $11,968,500.53 |
| APR/USDT:USDT | +55.12% | $2,432,147.21 |
| BTW/USDT:USDT | +25.91% | $20,802,848.57 |
| TAG/USDT:USDT | +23.11% | $2,969,539.15 |
| SYN/USDT:USDT | +15.53% | $5,757,337.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.93% | +4.56% |
| BEAT/USDT:USDT | below_1h_threshold | +4.74% | +4.37% |
| AIN/USDT:USDT | below_1h_threshold | +3.96% | +3.59% |
| CHIP/USDT:USDT | below_1h_threshold | +3.20% | +2.83% |
| HUMA/USDT:USDT | below_1h_threshold | +2.92% | +2.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
