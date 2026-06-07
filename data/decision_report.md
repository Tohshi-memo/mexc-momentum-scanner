# Decision Report

- generated_at: 2026-06-07T19:22:23.665885+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5994**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5994, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.36% | **-0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| ASK | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.69% | **+3.79%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.89% | **+0.58%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.56% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.88** / 初期 $100.00 (+48.88%)
- 確定: 1111件 (Win 268 / Loss 335 / Flat 508) / skip 1444件
- 成長率目線: 平均log +0.000358 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $148.88

## 4. Latest Market Context

- 更新: 2026-06-07T19:22:20.158183+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.93% price=61419.5
- Funnel: target 768 → liquid 125 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.7 >= 65=1, 4h RSI 79.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +22.23% | $3,102,019.74 |
| EPIC/USDT:USDT | +13.06% | $1,124,142.92 |
| BTW/USDT:USDT | +10.20% | $14,385,705.40 |
| BEAT/USDT:USDT | +8.15% | $53,284,331.08 |
| VELVET/USDT:USDT | +6.62% | $2,856,204.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UKOIL/USDT:USDT | below_1h_threshold | +1.77% | +2.71% |
| USOIL/USDT:USDT | below_1h_threshold | +1.60% | +2.53% |
| VELVET/USDT:USDT | below_1h_threshold | +1.15% | +2.09% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.98% | +1.91% |
| ALLO/USDT:USDT | below_1h_threshold | +0.64% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
