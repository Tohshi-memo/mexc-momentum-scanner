# Decision Report

- generated_at: 2026-05-30T01:54:49.671825+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5089**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5089, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.40% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.17% | **+0.17%** |
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +3.11% | **+0.93%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +2.73% | **+0.55%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.83% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 748件 (Win 175 / Loss 226 / Flat 347) / skip 902件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-30T01:54:46.141726+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=73585.9
- Funnel: target 773 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.8 >= 65=1, 4h RSI 82.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XLM/USDT:USDT | +27.26% | $425,424,214.86 |
| OL/USDT:USDT | +18.11% | $1,510,445.14 |
| LAB/USDT:USDT | +15.88% | $133,176,928.25 |
| HBAR/USDT:USDT | +15.79% | $39,197,744.99 |
| ALGO/USDT:USDT | +15.19% | $6,826,138.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +4.16% | +4.00% |
| ALLO/USDT:USDT | below_1h_threshold | +2.74% | +2.58% |
| VET/USDT:USDT | below_1h_threshold | +2.29% | +2.13% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.25% | +2.09% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.19% | +2.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
