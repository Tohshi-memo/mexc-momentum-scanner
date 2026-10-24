# Decision Report

- generated_at: 2026-10-24T01:21:18.672728+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17315**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17315, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 11/20 | 55.0% | +2.69% | **+1.48%** |
| LIMIT_6PCT | 11/20 | 55.0% | +1.99% | **+1.09%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_5PCT | 13/20 | 65.0% | +1.00% | **+0.65%** |
| LIMIT_9PCT | 8/20 | 40.0% | +1.57% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +1.83% | **+1.19%** |
| LIMIT_BB3S_LONG | 6/11 | 54.5% | +1.67% | **+0.91%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.77% | **+0.71%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,303.97** / 初期 $100.00 (+1203.97%)
- 確定: 6569件 (Win 1904 / Loss 2099 / Flat 2566) / skip 7307件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIRB/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $1,303.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6797件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0763 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5476件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T01:21:06.435592+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=80758.2
- Funnel: target 1088 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +88.03% | $5,909,071.05 |
| IRYS/USDT:USDT | +41.70% | $96,953,518.77 |
| AXIS/USDT:USDT | +24.06% | $1,986,102.78 |
| AGT/USDT:USDT | +14.89% | $10,878,186.23 |
| ARK/USDT:USDT | +4.52% | $1,997,945.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARK/USDT:USDT | below_1h_threshold | +4.82% | +4.61% |
| BIRB/USDT:USDT | below_1h_threshold | +2.89% | +2.68% |
| EDGE/USDT:USDT | below_1h_threshold | +0.93% | +0.72% |
| QNT/USDT:USDT | below_1h_threshold | +0.92% | +0.70% |
| S/USDT:USDT | below_1h_threshold | +0.77% | +0.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
