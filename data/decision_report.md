# Decision Report

- generated_at: 2026-05-10T20:57:38.309157+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3990**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.96% / filled 20/20。**
- 全期間 MARKET基準: n=3990, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.02% | **+0.97%** |
| ASK | 20/20 | 100.0% | +0.97% | **+0.97%** |
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.13% | **+0.85%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.52% | **+1.22%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.64% | **+0.61%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.21% | **+0.11%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.14% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.26** / 初期 $100.00 (+8.26%)
- 確定: 200件 (Win 49 / Loss 67 / Flat 84) / skip 351件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TROLLSOL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $108.26

## 4. Latest Market Context

- 更新: 2026-05-10T20:57:35.377133+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.97% price=80611.1
- Funnel: target 769 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +28.69% | $2,762,839.44 |
| ALCH/USDT:USDT | +23.12% | $2,957,647.54 |
| B/USDT:USDT | +13.83% | $2,256,772.30 |
| TROLLSOL/USDT:USDT | +10.36% | $4,280,087.18 |
| SUI/USDT:USDT | +9.61% | $695,348,892.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OG/USDT:USDT | below_1h_threshold | +3.10% | +4.07% |
| TRIA/USDT:USDT | below_1h_threshold | +2.90% | +3.87% |
| UKOIL/USDT:USDT | below_1h_threshold | +2.76% | +3.72% |
| USOIL/USDT:USDT | below_1h_threshold | +2.46% | +3.43% |
| BAS/USDT:USDT | below_1h_threshold | +1.92% | +2.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
