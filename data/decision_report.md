# Decision Report

- generated_at: 2026-07-30T16:41:27.013343+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9906**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9906, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.70% | **-2.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.01% | **+0.35%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.22% | **-0.18%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -1.31% | **-0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.90% | **+2.90%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +3.54% | **+2.13%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +4.08% | **+1.84%** |
| LIMIT_ATR_LONG | 5/20 | 25.0% | +2.44% | **+0.61%** |
| LIMIT_FIB1272_LONG | 2/20 | 10.0% | +2.82% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3520件 (Win 1113 / Loss 1147 / Flat 1260) / skip 2947件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2074件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0109 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.82** / 初期 $100.00 (+10.82%)
- 確定: 801件 (Win 261 / Loss 317 / Flat 223) / pending 4件 / skip 587件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000246 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $110.82

## 6. Latest Market Context

- 更新: 2026-07-30T16:41:19.849338+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64762.0
- Funnel: target 920 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +5.67% | $1,661,751.57 |
| CAP/USDT:USDT | +4.35% | $2,519,898.96 |
| UAI/USDT:USDT | +4.28% | $25,039,447.34 |
| EVAA/USDT:USDT | +3.95% | $1,657,556.40 |
| ZHIPUSTOCK/USDT:USDT | +2.68% | $3,941,714.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +4.36% | +4.26% |
| UAI/USDT:USDT | below_1h_threshold | +4.22% | +4.11% |
| EVAA/USDT:USDT | below_1h_threshold | +3.79% | +3.68% |
| KORU/USDT:USDT | below_1h_threshold | +3.53% | +3.43% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.66% | +2.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
