# Decision Report

- generated_at: 2026-09-26T11:01:20.712682+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15596**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15596, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.57% | **-1.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +3.30% | **+0.99%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.72% | **+0.64%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.08% | **+1.66%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.70% | **+1.45%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.83% | **+1.41%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.06% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,268.86** / 初期 $100.00 (+1168.86%)
- 確定: 5957件 (Win 1760 / Loss 1911 / Flat 2286) / skip 6200件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PAID/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,268.86

## 4. Robust Adaptive DryRun ($100)

- 残高: **$266.84** / 初期 $100.00 (+166.84%)
- 確定: 3526件 (Win 973 / Loss 806 / Flat 1747) / skip 5481件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0644 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PAID/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $266.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 3186件 (Win 937 / Loss 1262 / Flat 987) / pending 0件 / skip 3880件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000383 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-26T11:01:10.381350+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=84135.2
- Funnel: target 1067 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +333.33% | $2,224,339.90 |
| RARE/USDT:USDT | +45.80% | $5,258,430.87 |
| 2Z/USDT:USDT | +30.40% | $2,987,271.57 |
| BR/USDT:USDT | +28.27% | $10,584,204.54 |
| BATON/USDT:USDT | +21.11% | $1,316,636.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +2.71% | +2.71% |
| 2Z/USDT:USDT | below_1h_threshold | +1.23% | +1.23% |
| MUBARAK/USDT:USDT | below_1h_threshold | +0.58% | +0.58% |
| BEAT/USDT:USDT | below_1h_threshold | +0.49% | +0.49% |
| GALA/USDT:USDT | below_1h_threshold | +0.45% | +0.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
