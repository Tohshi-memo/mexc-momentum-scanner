# Decision Report

- generated_at: 2026-05-06T13:02:55.812530+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3459**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3459, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.88% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.88% | **+0.69%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.39% | **+0.66%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.74% | **+0.52%** |
| LIMIT_BB3S | 5/16 | 31.2% | +0.21% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| ASK_LONG | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.57% | **+0.94%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.11% | **+0.56%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +0.61% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 11件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T13:02:53.020825+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=82113.8
- Funnel: target 770 → liquid 197 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +94.04% | $2,289,781.67 |
| FHE/USDT:USDT | +40.78% | $31,981,491.71 |
| TONCOIN/USDT:USDT | +36.46% | $219,873,889.05 |
| IO/USDT:USDT | +34.52% | $14,380,492.55 |
| BILL/USDT:USDT | +34.47% | $4,575,362.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +1.12% | +1.21% |
| IO/USDT:USDT | below_1h_threshold | +0.83% | +0.92% |
| M/USDT:USDT | below_1h_threshold | +0.45% | +0.54% |
| XMR/USDT:USDT | below_1h_threshold | +0.35% | +0.44% |
| NOT/USDT:USDT | below_1h_threshold | +0.18% | +0.27% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
