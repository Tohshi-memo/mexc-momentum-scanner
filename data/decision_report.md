# Decision Report

- generated_at: 2026-09-07T07:56:23.728357+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13873**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13873, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.17% | **-1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.79% | **+0.47%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.28% | **+2.05%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.31% | **+1.62%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.08% | **+1.25%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.30% | **+1.15%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.05% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$857.63** / 初期 $100.00 (+757.63%)
- 確定: 5146件 (Win 1542 / Loss 1681 / Flat 1923) / skip 5288件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_8PCT` TP_HIT account +1.00% 残高後 $857.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2571件 (Win 717 / Loss 618 / Flat 1236) / skip 4713件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0879 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.02** / 初期 $100.00 (+20.02%)
- 確定: 2465件 (Win 732 / Loss 936 / Flat 797) / pending 3件 / skip 2875件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000371 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_8PCT` TP_HIT account +0.34% 残高後 $120.02

## 6. Latest Market Context

- 更新: 2026-09-07T07:56:11.623578+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=79305.3
- Funnel: target 1059 → liquid 143 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +323.25% | $1,760,805.60 |
| BONER/USDT:USDT | +130.21% | $5,228,625.25 |
| CATI/USDT:USDT | +12.86% | $1,024,179.26 |
| XAN/USDT:USDT | +12.42% | $2,342,489.12 |
| ICP/USDT:USDT | +12.10% | $10,460,209.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +2.24% | +2.63% |
| ICP/USDT:USDT | below_1h_threshold | +2.11% | +2.50% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.99% | +2.38% |
| BONER/USDT:USDT | below_1h_threshold | +1.98% | +2.37% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.79% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
