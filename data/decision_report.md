# Decision Report

- generated_at: 2026-05-19T19:54:09.722327+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4498**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4498, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +2.54% | **+1.27%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_BB3S | 6/11 | 54.5% | +1.05% | **+0.57%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +3.39% | **+1.88%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.39% | **+1.87%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.01% | **+1.51%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.12% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 586件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T19:54:07.803772+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=76828.8
- Funnel: target 760 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +58.20% | $21,913,065.20 |
| EDEN/USDT:USDT | +27.22% | $12,131,161.15 |
| VVV/USDT:USDT | +14.65% | $10,449,008.49 |
| LAB/USDT:USDT | +9.65% | $86,197,440.86 |
| LIT/USDT:USDT | +8.43% | $2,060,329.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.30% | +4.22% |
| LAB/USDT:USDT | below_1h_threshold | +3.54% | +3.45% |
| PLAY/USDT:USDT | below_1h_threshold | +2.64% | +2.55% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.31% | +2.22% |
| VVV/USDT:USDT | below_1h_threshold | +2.11% | +2.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
