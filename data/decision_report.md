# Decision Report

- generated_at: 2026-05-08T15:57:48.704952+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3799**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.57% / filled 20/20。**
- 全期間 MARKET基準: n=3799, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+2.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.57% | **+2.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.69% | **+2.69%** |
| MARKET | 20/20 | 100.0% | +2.57% | **+2.57%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.95% | **+1.56%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.47% | **+0.88%** |
| LIMIT_3PCT | 8/20 | 40.0% | +0.44% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.02% | **+0.46%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.33% | **+0.17%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | -0.32% | **-0.22%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.62% | **-0.31%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | -0.47% | **-0.34%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 168件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T15:57:44.494543+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80148.7
- Funnel: target 773 → liquid 183 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.6 >= 65=1, 4h RSI 88.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +58.25% | $16,038,245.89 |
| PHAROS/USDT:USDT | +42.71% | $13,603,264.96 |
| SPORTFUN/USDT:USDT | +38.06% | $1,105,504.92 |
| COLLECT/USDT:USDT | +33.33% | $1,338,739.82 |
| STRK/USDT:USDT | +30.06% | $29,705,537.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.66% | +4.62% |
| WLD/USDT:USDT | below_1h_threshold | +3.46% | +3.41% |
| JUP/USDT:USDT | below_1h_threshold | +3.44% | +3.40% |
| SPORTFUN/USDT:USDT | below_1h_threshold | +3.08% | +3.04% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.79% | +2.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
