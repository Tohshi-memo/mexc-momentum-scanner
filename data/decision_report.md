# Decision Report

- generated_at: 2026-05-10T02:37:42.797496+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3935**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3935, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_BB3S | 2/18 | 11.1% | +2.90% | **+0.32%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.36% | **+0.32%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.34% | **+1.17%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.33% | **+1.16%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.15% | **+0.64%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.67% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 196件 (Win 48 / Loss 66 / Flat 82) / skip 300件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T02:37:39.459354+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=80748.8
- Funnel: target 769 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +34.82% | $6,235,549.13 |
| INX/USDT:USDT | +26.58% | $13,703,109.76 |
| LAYER/USDT:USDT | +21.97% | $1,069,204.25 |
| AGT/USDT:USDT | +18.41% | $1,226,811.31 |
| AIGENSYN/USDT:USDT | +13.09% | $1,129,157.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.83% | +2.71% |
| BABY/USDT:USDT | below_1h_threshold | +2.46% | +2.34% |
| TURBO/USDT:USDT | below_1h_threshold | +2.26% | +2.14% |
| ORDI/USDT:USDT | below_1h_threshold | +2.19% | +2.07% |
| PLAY/USDT:USDT | below_1h_threshold | +2.11% | +2.00% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
