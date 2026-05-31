# Decision Report

- generated_at: 2026-05-31T17:11:35.220220+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5209**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5209, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.68% | **-1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.27% | **+0.23%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.01% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.35% | **+1.68%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.61% | **+1.56%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.36% | **+1.42%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.65% | **+1.24%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.88** / 初期 $100.00 (+29.88%)
- 確定: 844件 (Win 196 / Loss 251 / Flat 397) / skip 926件
- 成長率目線: 平均log +0.000310 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.72% 残高後 $129.88

## 4. Latest Market Context

- 更新: 2026-05-31T17:11:32.658624+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=73444.9
- Funnel: target 773 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +11.15% | $10,399,779.21 |
| AIA/USDT:USDT | +7.04% | $5,553,852.89 |
| HOME/USDT:USDT | +5.85% | $1,791,410.04 |
| STG/USDT:USDT | +5.16% | $5,640,619.72 |
| BILL/USDT:USDT | +2.45% | $5,570,517.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +1.71% | +1.78% |
| NEX/USDT:USDT | below_1h_threshold | +1.64% | +1.71% |
| AIA/USDT:USDT | below_1h_threshold | +1.60% | +1.68% |
| BILL/USDT:USDT | below_1h_threshold | +1.43% | +1.50% |
| BEAT/USDT:USDT | below_1h_threshold | +0.87% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
