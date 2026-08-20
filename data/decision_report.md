# Decision Report

- generated_at: 2026-08-20T16:56:22.535629+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12060**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12060, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.62% | **-0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -1.09% | **-0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.54% | **+1.23%** |
| MARKET_LONG | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.29% | **+0.84%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.68% | **+0.41%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.44% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$600.96** / 初期 $100.00 (+500.96%)
- 確定: 4273件 (Win 1307 / Loss 1397 / Flat 1569) / skip 4348件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.20%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $600.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3649件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.48** / 初期 $100.00 (+16.48%)
- 確定: 1758件 (Win 521 / Loss 673 / Flat 564) / pending 1件 / skip 1777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.48

## 6. Latest Market Context

- 更新: 2026-08-20T16:56:13.752291+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=72620.0
- Funnel: target 1011 → liquid 203 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1, 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +9.84% | $1,053,738.59 |
| PEOPLE/USDT:USDT | +8.32% | $1,418,704.90 |
| ALLO/USDT:USDT | +4.64% | $2,375,710.25 |
| ONG/USDT:USDT | +4.05% | $4,329,973.46 |
| PIPPIN/USDT:USDT | +3.93% | $1,819,015.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.58% | +4.32% |
| ONG/USDT:USDT | below_1h_threshold | +4.06% | +3.80% |
| PIPPIN/USDT:USDT | below_1h_threshold | +3.94% | +3.68% |
| NIULAI/USDT:USDT | below_1h_threshold | +3.74% | +3.48% |
| FILECOIN/USDT:USDT | below_1h_threshold | +3.69% | +3.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
