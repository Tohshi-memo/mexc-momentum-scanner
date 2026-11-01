# Decision Report

- generated_at: 2026-11-01T17:46:44.043789+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17986**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17986, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +7.14% | **+1.79%** |
| LIMIT_7PCT | 7/20 | 35.0% | +5.03% | **+1.76%** |
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_6PCT | 8/20 | 40.0% | +2.68% | **+1.07%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.21% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.63% | **+2.72%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.76% | **+2.63%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.70% | **+2.16%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.75% | **+1.51%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,517.20** / 初期 $100.00 (+1417.20%)
- 確定: 6839件 (Win 1984 / Loss 2196 / Flat 2659) / skip 7708件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,517.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$375.58** / 初期 $100.00 (+275.58%)
- 確定: 4427件 (Win 1188 / Loss 984 / Flat 2255) / skip 6970件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0543 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $375.58

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6147件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000262 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-01T17:46:25.224135+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=78038.9
- Funnel: target 1088 → liquid 121 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.6 >= 65=1, 4h RSI 79.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +35.71% | $7,500,495.05 |
| IDOL/USDT:USDT | +11.60% | $8,819,267.97 |
| BEAMX/USDT:USDT | +7.09% | $2,598,957.56 |
| RT/USDT:USDT | +2.70% | $1,462,661.76 |
| EVAA/USDT:USDT | +2.00% | $9,408,294.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAMX/USDT:USDT | below_1h_threshold | +2.36% | +2.46% |
| AIN/USDT:USDT | below_1h_threshold | +1.71% | +1.80% |
| EVAA/USDT:USDT | below_1h_threshold | +1.62% | +1.71% |
| NIGHT/USDT:USDT | below_1h_threshold | +0.76% | +0.85% |
| DOT/USDT:USDT | below_1h_threshold | +0.67% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
