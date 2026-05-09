# Decision Report

- generated_at: 2026-05-09T15:43:13.420359+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3893**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3893, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/14 | 28.6% | +3.54% | **+1.01%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.99% | **+0.69%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.45% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.25% | **+1.13%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.35% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.27** / 初期 $100.00 (+8.27%)
- 確定: 195件 (Win 48 / Loss 65 / Flat 82) / skip 259件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +3.61%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $108.27

## 4. Latest Market Context

- 更新: 2026-05-09T15:43:10.061781+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80482.3
- Funnel: target 769 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PTB/USDT:USDT | +42.02% | $1,117,751.32 |
| INX/USDT:USDT | +38.46% | $1,712,464.82 |
| ZEREBRO/USDT:USDT | +31.33% | $3,745,793.24 |
| SAHARA/USDT:USDT | +31.11% | $5,478,125.58 |
| SATO/USDT:USDT | +30.15% | $3,482,816.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCA/USDT:USDT | below_relative_strength | +5.09% | +4.85% |
| LAB/USDT:USDT | below_1h_threshold | +4.40% | +4.16% |
| INX/USDT:USDT | below_1h_threshold | +3.69% | +3.45% |
| BIO/USDT:USDT | below_1h_threshold | +3.37% | +3.14% |
| SIREN/USDT:USDT | below_1h_threshold | +2.97% | +2.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
