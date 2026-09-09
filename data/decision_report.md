# Decision Report

- generated_at: 2026-09-09T23:11:16.918925+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14129**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.68% / filled 20/20。**
- 全期間 MARKET基準: n=14129, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.68% | **+3.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +4.12% | **+3.71%** |
| MARKET | 20/20 | 100.0% | +3.68% | **+3.68%** |
| LIMIT_2PCT | 12/20 | 60.0% | +4.42% | **+2.65%** |
| LIMIT_ATR | 12/20 | 60.0% | +3.29% | **+1.98%** |
| LIMIT_BB3S | 9/19 | 47.4% | +1.96% | **+0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.05% | **+1.03%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.73% | **-0.44%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5377件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$195.40** / 初期 $100.00 (+95.40%)
- 確定: 2723件 (Win 747 / Loss 638 / Flat 1338) / skip 4817件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0467 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $195.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.53** / 初期 $100.00 (+18.53%)
- 確定: 2634件 (Win 771 / Loss 1008 / Flat 855) / pending 2件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000370 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.53

## 6. Latest Market Context

- 更新: 2026-09-09T23:11:04.975680+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=78167.1
- Funnel: target 1064 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +20.22% | $2,799,279.63 |
| BTR/USDT:USDT | +14.01% | $1,893,449.39 |
| IOST/USDT:USDT | +9.50% | $39,474,996.98 |
| KAS/USDT:USDT | +3.26% | $3,878,084.01 |
| XMR/USDT:USDT | +2.04% | $5,581,187.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +3.89% | +3.54% |
| AKE/USDT:USDT | below_1h_threshold | +2.23% | +1.88% |
| UAI/USDT:USDT | below_1h_threshold | +1.79% | +1.43% |
| STX/USDT:USDT | below_1h_threshold | +1.57% | +1.21% |
| INJ/USDT:USDT | below_1h_threshold | +1.26% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
