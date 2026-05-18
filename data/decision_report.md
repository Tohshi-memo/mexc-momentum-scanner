# Decision Report

- generated_at: 2026-05-18T06:03:25.967924+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4437**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4437, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.24% | **+0.09%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| ASK | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.71% | **+1.71%** |
| MARKET_LONG | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.03% | **+0.72%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.54% | **+0.32%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.47% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$96.22** / 初期 $100.00 (-3.78%)
- 確定トレード: 52件 (TP 13 / SL 36 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.22
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.70** / 初期 $100.00 (+21.70%)
- 確定: 434件 (Win 113 / Loss 147 / Flat 174) / skip 564件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $121.70

## 4. Latest Market Context

- 更新: 2026-05-18T06:03:23.957864+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=76899.6
- Funnel: target 765 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +45.96% | $6,658,689.04 |
| BSB/USDT:USDT | +9.27% | $19,557,512.79 |
| OPENLEDGER/USDT:USDT | +5.03% | $1,294,450.73 |
| AKT/USDT:USDT | +4.99% | $1,551,690.89 |
| HYPE/USDT:USDT | +4.17% | $275,433,894.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +1.27% | +1.25% |
| PLAY/USDT:USDT | below_1h_threshold | +0.72% | +0.71% |
| ATOM/USDT:USDT | below_1h_threshold | +0.68% | +0.66% |
| FIDA/USDT:USDT | below_1h_threshold | +0.59% | +0.57% |
| RIVER/USDT:USDT | below_1h_threshold | +0.41% | +0.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
