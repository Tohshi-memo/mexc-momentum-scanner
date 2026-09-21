# Decision Report

- generated_at: 2026-09-21T13:36:23.759363+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15260**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15260, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.25% | **-1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_BB3S | 9/15 | 60.0% | +1.05% | **+0.63%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.59% | **+0.41%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +4.15% | **+2.28%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.79% | **+1.96%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.09% | **+1.85%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.41% | **+1.81%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.45% | **+1.73%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,172.18** / 初期 $100.00 (+1072.18%)
- 確定: 5751件 (Win 1713 / Loss 1849 / Flat 2189) / skip 6070件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,172.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3315件 (Win 915 / Loss 765 / Flat 1635) / skip 5356件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0051 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.26** / 初期 $100.00 (+22.26%)
- 確定: 3036件 (Win 892 / Loss 1188 / Flat 956) / pending 3件 / skip 3691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000078 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $122.26

## 6. Latest Market Context

- 更新: 2026-09-21T13:36:12.558102+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=85119.1
- Funnel: target 1055 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +63.80% | $8,531,000.83 |
| PHA/USDT:USDT | +59.04% | $6,005,411.12 |
| UAI/USDT:USDT | +38.15% | $2,297,059.36 |
| PTB/USDT:USDT | +34.59% | $1,196,773.61 |
| NIL/USDT:USDT | +28.98% | $7,978,256.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.78% | +3.97% |
| EVAA/USDT:USDT | below_1h_threshold | +1.80% | +1.98% |
| WIF/USDT:USDT | below_1h_threshold | +1.69% | +1.87% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.53% | +1.72% |
| ONE/USDT:USDT | below_1h_threshold | +1.47% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
