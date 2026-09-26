# Decision Report

- generated_at: 2026-09-26T09:12:05.416710+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15589**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15589, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.78% | **+0.67%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.80% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.87% | **+1.29%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.36% | **+1.22%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.21% | **+0.88%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,253.08** / 初期 $100.00 (+1153.08%)
- 確定: 5950件 (Win 1757 / Loss 1909 / Flat 2284) / skip 6200件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,253.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.48** / 初期 $100.00 (+163.48%)
- 確定: 3519件 (Win 969 / Loss 804 / Flat 1746) / skip 5481件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0790 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $263.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 3186件 (Win 937 / Loss 1262 / Flat 987) / pending 0件 / skip 3874件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000300 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-26T09:11:52.320401+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=84070.0
- Funnel: target 1067 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +340.43% | $1,949,479.21 |
| BATON/USDT:USDT | +33.58% | $1,399,106.12 |
| RARE/USDT:USDT | +30.88% | $4,306,340.31 |
| 2Z/USDT:USDT | +27.94% | $1,615,521.00 |
| ARK/USDT:USDT | +23.99% | $4,031,049.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +1.70% | +1.81% |
| QNT/USDT:USDT | below_1h_threshold | +1.18% | +1.30% |
| TAO/USDT:USDT | below_1h_threshold | +1.08% | +1.20% |
| ARK/USDT:USDT | below_1h_threshold | +0.89% | +1.00% |
| PYTH/USDT:USDT | below_1h_threshold | +0.69% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
