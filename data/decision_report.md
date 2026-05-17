# Decision Report

- generated_at: 2026-05-17T11:33:19.228561+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4396**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4396, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 5/20 | 25.0% | +2.35% | **+0.59%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.28% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.13% | **+1.28%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.11% | **+1.27%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.68% | **+1.26%** |
| ASK_LONG | 20/20 | 100.0% | +1.24% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.21% | **+1.21%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.10** / 初期 $100.00 (+18.10%)
- 確定: 396件 (Win 100 / Loss 137 / Flat 159) / skip 561件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $118.10

## 4. Latest Market Context

- 更新: 2026-05-17T11:33:17.260897+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=78288.8
- Funnel: target 760 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +41.19% | $9,042,374.83 |
| CGPT/USDT:USDT | +21.51% | $2,332,633.00 |
| AIA/USDT:USDT | +20.77% | $13,489,131.49 |
| ASTEROID/USDT:USDT | +14.20% | $4,411,817.26 |
| KAIA/USDT:USDT | +13.08% | $1,408,813.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_1h_threshold | +3.67% | +3.84% |
| BEAT/USDT:USDT | below_1h_threshold | +2.89% | +3.06% |
| KAIA/USDT:USDT | below_1h_threshold | +2.69% | +2.86% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.58% | +2.76% |
| BILL/USDT:USDT | below_1h_threshold | +1.49% | +1.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
