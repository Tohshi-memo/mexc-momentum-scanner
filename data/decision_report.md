# Decision Report

- generated_at: 2026-05-11T23:48:01.237903+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4076**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4076, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.48% | **+0.19%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.17% | **+0.16%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.13% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +6.11% | **+2.04%** |
| ASK_LONG | 20/20 | 100.0% | +1.89% | **+1.89%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.61% | **+1.21%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 419件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T23:47:58.086289+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=81698.6
- Funnel: target 757 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PENGUIN/USDT:USDT | +22.37% | $3,035,934.62 |
| GIGA/USDT:USDT | +20.49% | $1,055,323.10 |
| USELESS/USDT:USDT | +16.72% | $3,687,609.56 |
| RIF/USDT:USDT | +15.22% | $1,504,695.94 |
| B/USDT:USDT | +11.51% | $39,674,498.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UP/USDT:USDT | below_1h_threshold | +2.47% | +2.58% |
| H/USDT:USDT | below_1h_threshold | +1.95% | +2.06% |
| GIGA/USDT:USDT | below_1h_threshold | +1.67% | +1.78% |
| RIF/USDT:USDT | below_1h_threshold | +1.59% | +1.70% |
| USELESS/USDT:USDT | below_1h_threshold | +1.43% | +1.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
