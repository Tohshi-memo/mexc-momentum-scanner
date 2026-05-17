# Decision Report

- generated_at: 2026-05-17T16:13:27.281651+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4410**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4410, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.08% | **-1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.03% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.74% | **+1.92%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.67% | **+1.25%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.85% | **+1.11%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.79% | **+0.89%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.95** / 初期 $100.00 (+18.95%)
- 確定: 407件 (Win 105 / Loss 138 / Flat 164) / skip 564件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $118.95

## 4. Latest Market Context

- 更新: 2026-05-17T16:13:25.319767+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78017.3
- Funnel: target 760 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +4.06% | $3,748,688.91 |
| FHE/USDT:USDT | +3.28% | $3,757,434.76 |
| RAVE/USDT:USDT | +2.83% | $4,563,532.57 |
| APE/USDT:USDT | +1.82% | $3,526,789.10 |
| GUA/USDT:USDT | +1.30% | $2,777,714.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +4.26% | +4.25% |
| FHE/USDT:USDT | below_1h_threshold | +3.31% | +3.30% |
| RAVE/USDT:USDT | below_1h_threshold | +2.80% | +2.78% |
| APE/USDT:USDT | below_1h_threshold | +1.83% | +1.82% |
| GUA/USDT:USDT | below_1h_threshold | +1.59% | +1.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
