# Decision Report

- generated_at: 2026-06-03T07:13:39.480028+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5528**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5528, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.80% | **-1.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.81% | **+1.40%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.45% | **+1.10%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.10% | **+0.77%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.18% | **+0.71%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.07** / 初期 $100.00 (+30.07%)
- 確定: 982件 (Win 231 / Loss 303 / Flat 448) / skip 1107件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $130.07

## 4. Latest Market Context

- 更新: 2026-06-03T07:13:37.134705+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=67111.7
- Funnel: target 773 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLO/USDT:USDT | +31.31% | $3,039,773.06 |
| PORTAL/USDT:USDT | +30.43% | $14,198,411.73 |
| GENIUS/USDT:USDT | +27.59% | $1,814,311.97 |
| LIT/USDT:USDT | +23.02% | $7,920,344.85 |
| ENA/USDT:USDT | +22.82% | $45,610,534.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +2.73% | +2.49% |
| US/USDT:USDT | below_1h_threshold | +2.23% | +1.99% |
| WLD/USDT:USDT | below_1h_threshold | +2.15% | +1.90% |
| ENA/USDT:USDT | below_1h_threshold | +2.10% | +1.86% |
| WIF/USDT:USDT | below_1h_threshold | +1.90% | +1.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
