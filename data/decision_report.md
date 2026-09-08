# Decision Report

- generated_at: 2026-09-08T20:56:32.951161+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14020**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.85% / filled 20/20。**
- 全期間 MARKET基準: n=14020, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.89% | **+0.67%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.01% | **+0.25%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_BB3S | 3/10 | 30.0% | +0.28% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.46% | **+0.37%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +0.56% | **+0.25%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.13% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,013.58** / 初期 $100.00 (+913.58%)
- 確定: 5284件 (Win 1588 / Loss 1707 / Flat 1989) / skip 5297件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOGS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,013.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.66** / 初期 $100.00 (+90.66%)
- 確定: 2623件 (Win 726 / Loss 622 / Flat 1275) / skip 4808件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0347 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DOGS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $190.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.49** / 初期 $100.00 (+19.49%)
- 確定: 2603件 (Win 762 / Loss 989 / Flat 852) / pending 3件 / skip 2885件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000285 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DOGS/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $119.49

## 6. Latest Market Context

- 更新: 2026-09-08T20:56:17.941798+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78468.2
- Funnel: target 1070 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAY/USDT:USDT | +8.65% | $2,449,589.85 |
| ARX/USDT:USDT | +6.87% | $1,055,012.16 |
| FF/USDT:USDT | +6.30% | $1,635,028.35 |
| BTR/USDT:USDT | +3.77% | $1,183,299.25 |
| EGLD/USDT:USDT | +3.76% | $1,556,297.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +3.41% | +3.33% |
| FF/USDT:USDT | below_1h_threshold | +2.55% | +2.47% |
| XAN/USDT:USDT | below_1h_threshold | +2.00% | +1.92% |
| SOLV/USDT:USDT | below_1h_threshold | +1.72% | +1.64% |
| ATOM/USDT:USDT | below_1h_threshold | +1.28% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
