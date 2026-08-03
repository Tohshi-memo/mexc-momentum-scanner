# Decision Report

- generated_at: 2026-08-03T17:11:19.503882+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10237**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10237, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.71% | **-2.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.09% | **+0.54%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.13% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +4.17% | **+2.50%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +5.25% | **+2.36%** |
| MARKET_LONG | 20/20 | 100.0% | +1.91% | **+1.91%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +4.16% | **+1.66%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.69% | **+1.64%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$594.17** / 初期 $100.00 (+494.17%)
- 確定: 3695件 (Win 1173 / Loss 1208 / Flat 1314) / skip 3103件
- 成長率目線: 平均log +0.000482 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $594.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2365件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0320 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.18** / 初期 $100.00 (+17.18%)
- 確定: 1020件 (Win 330 / Loss 394 / Flat 296) / pending 5件 / skip 686件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000524 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.18

## 6. Latest Market Context

- 更新: 2026-08-03T17:11:10.740499+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63755.0
- Funnel: target 929 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +14.08% | $5,846,110.14 |
| PIPPIN/USDT:USDT | +8.99% | $1,877,470.55 |
| UB/USDT:USDT | +5.70% | $3,380,846.98 |
| SKYAI/USDT:USDT | +4.69% | $8,443,822.68 |
| HOME/USDT:USDT | +4.35% | $3,177,462.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +3.12% | +3.10% |
| COTI/USDT:USDT | below_1h_threshold | +2.46% | +2.43% |
| CATE/USDT:USDT | below_1h_threshold | +2.21% | +2.18% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +1.76% | +1.73% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.71% | +1.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
