# Decision Report

- generated_at: 2026-05-31T20:11:45.445171+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5224**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5224, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.65% | **+1.06%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.59% | **+0.88%** |
| LIMIT_BB3S | 11/19 | 57.9% | +0.39% | **+0.23%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.54% | **+1.77%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.98% | **+1.49%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.03% | **+1.12%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.78% | **+1.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.16** / 初期 $100.00 (+31.16%)
- 確定: 859件 (Win 199 / Loss 255 / Flat 405) / skip 926件
- 成長率目線: 平均log +0.000316 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIANRENSHENG/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $131.16

## 4. Latest Market Context

- 更新: 2026-05-31T20:11:42.885639+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=73642.9
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +41.09% | $14,636,429.95 |
| BIANRENSHENG/USDT:USDT | +15.08% | $2,940,899.47 |
| ZORA/USDT:USDT | +11.78% | $1,353,217.37 |
| UB/USDT:USDT | +10.88% | $6,947,855.03 |
| HOME/USDT:USDT | +10.07% | $2,610,143.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +4.02% | +3.85% |
| STG/USDT:USDT | below_1h_threshold | +3.97% | +3.81% |
| ALLO/USDT:USDT | below_1h_threshold | +1.77% | +1.61% |
| HOME/USDT:USDT | below_1h_threshold | +1.56% | +1.39% |
| DYDX/USDT:USDT | below_1h_threshold | +1.42% | +1.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
