# Decision Report

- generated_at: 2026-09-23T07:46:35.906666+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15414**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15414, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.97% | **-1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +5.28% | **+1.59%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.27% | **+0.68%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +4.86% | **+3.40%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.94% | **+2.36%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.57% | **+1.80%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.57% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,222.14** / 初期 $100.00 (+1122.14%)
- 確定: 5887件 (Win 1738 / Loss 1884 / Flat 2265) / skip 6088件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAKE/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $1,222.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.15** / 初期 $100.00 (+149.15%)
- 確定: 3366件 (Win 929 / Loss 785 / Flat 1652) / skip 5459件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0255 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $249.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.98** / 初期 $100.00 (+20.98%)
- 確定: 3133件 (Win 921 / Loss 1233 / Flat 979) / pending 3件 / skip 3756件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000224 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $120.98

## 6. Latest Market Context

- 更新: 2026-09-23T07:46:19.844715+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=86116.3
- Funnel: target 1061 → liquid 190 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAKE/USDT:USDT | +193.42% | $1,620,899.36 |
| SHROOM/USDT:USDT | +80.22% | $1,310,304.85 |
| LONGXIA/USDT:USDT | +36.76% | $1,843,948.67 |
| NIL/USDT:USDT | +28.35% | $8,230,608.31 |
| SAGA/USDT:USDT | +24.60% | $1,794,486.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHROOM/USDT:USDT | below_1h_threshold | +4.22% | +4.58% |
| MYX/USDT:USDT | below_1h_threshold | +3.10% | +3.45% |
| NIL/USDT:USDT | below_1h_threshold | +2.04% | +2.40% |
| PENGU/USDT:USDT | below_1h_threshold | +1.23% | +1.59% |
| GRASS/USDT:USDT | below_1h_threshold | +0.97% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
