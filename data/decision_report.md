# Decision Report

- generated_at: 2026-05-09T19:22:39.112188+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3912**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3912, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.31% | **+0.09%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.46% | **+1.31%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.52% | **+1.06%** |
| LIMIT_BB3S_LONG | 9/10 | 90.0% | +1.06% | **+0.95%** |
| MARKET_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.27** / 初期 $100.00 (+8.27%)
- 確定: 195件 (Win 48 / Loss 65 / Flat 82) / skip 278件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +3.61%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $108.27

## 4. Latest Market Context

- 更新: 2026-05-09T19:22:36.196759+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=80865.2
- Funnel: target 769 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +16.46% | $25,638,083.45 |
| BILL/USDT:USDT | +12.48% | $33,572,183.00 |
| INX/USDT:USDT | +12.27% | $4,534,187.51 |
| MITO/USDT:USDT | +10.95% | $1,480,296.37 |
| JASMY/USDT:USDT | +10.35% | $6,412,316.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MITO/USDT:USDT | below_1h_threshold | +4.10% | +4.10% |
| BILL/USDT:USDT | below_1h_threshold | +2.51% | +2.51% |
| BIO/USDT:USDT | below_1h_threshold | +2.23% | +2.23% |
| INX/USDT:USDT | below_1h_threshold | +1.92% | +1.92% |
| AERO/USDT:USDT | below_1h_threshold | +1.82% | +1.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
