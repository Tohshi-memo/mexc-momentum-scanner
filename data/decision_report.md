# Decision Report

- generated_at: 2026-09-09T20:21:32.659567+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14117**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14117, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.62% | **+0.56%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.71% | **+2.44%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.43% | **+1.35%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.21% | **+0.88%** |
| MARKET_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5365件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$196.81** / 初期 $100.00 (+96.81%)
- 確定: 2711件 (Win 746 / Loss 634 / Flat 1331) / skip 4817件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1968 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $196.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.16** / 初期 $100.00 (+19.16%)
- 確定: 2628件 (Win 770 / Loss 1003 / Flat 855) / pending 3件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000557 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.16

## 6. Latest Market Context

- 更新: 2026-09-09T20:21:22.160804+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78214.3
- Funnel: target 1064 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IOST/USDT:USDT | +25.66% | $29,493,466.98 |
| COTI/USDT:USDT | +8.94% | $2,007,183.15 |
| SOCK/USDT:USDT | +8.80% | $1,607,997.56 |
| BTR/USDT:USDT | +7.69% | $1,258,931.76 |
| WAVES/USDT:USDT | +6.58% | $1,192,075.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WAVES/USDT:USDT | below_1h_threshold | +4.22% | +4.21% |
| CNPY/USDT:USDT | below_1h_threshold | +2.45% | +2.43% |
| BTR/USDT:USDT | below_1h_threshold | +1.16% | +1.14% |
| SOXL/USDT:USDT | below_1h_threshold | +0.82% | +0.81% |
| TAO/USDT:USDT | below_1h_threshold | +0.73% | +0.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
