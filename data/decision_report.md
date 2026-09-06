# Decision Report

- generated_at: 2026-09-06T07:46:20.421825+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13804**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13804, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_BB3S | 3/15 | 20.0% | +0.84% | **+0.17%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.18% | **+0.12%** |
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.23% | **+3.14%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.94% | **+1.45%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.47% | **+1.03%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.14% | **+0.68%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.83% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$860.59** / 初期 $100.00 (+760.59%)
- 確定: 5110件 (Win 1535 / Loss 1669 / Flat 1906) / skip 5255件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $860.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$193.56** / 初期 $100.00 (+93.56%)
- 確定: 2549件 (Win 713 / Loss 605 / Flat 1231) / skip 4666件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0191 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $193.56

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.33** / 初期 $100.00 (+20.33%)
- 確定: 2417件 (Win 721 / Loss 918 / Flat 778) / pending 3件 / skip 2855件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $120.33

## 6. Latest Market Context

- 更新: 2026-09-06T07:46:08.613078+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=79796.1
- Funnel: target 1054 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +46.39% | $142,869,937.94 |
| RAY/USDT:USDT | +28.92% | $2,853,965.69 |
| FLOCK/USDT:USDT | +27.02% | $1,226,671.68 |
| MAGMA/USDT:USDT | +19.53% | $2,464,973.45 |
| UAI/USDT:USDT | +15.27% | $12,513,283.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEAR/USDT:USDT | below_1h_threshold | +1.06% | +0.99% |
| SPX/USDT:USDT | below_1h_threshold | +0.74% | +0.66% |
| MONAD/USDT:USDT | below_1h_threshold | +0.62% | +0.55% |
| SOXL/USDT:USDT | below_1h_threshold | +0.60% | +0.53% |
| ATOM/USDT:USDT | below_1h_threshold | +0.51% | +0.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
