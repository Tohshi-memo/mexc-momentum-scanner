# Decision Report

- generated_at: 2026-10-15T01:26:21.881465+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16711**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16711, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.32% | **+0.53%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.33% | **+0.30%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.26% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +6.65% | **+5.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.92% | **+0.74%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.74% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 239件 (TP 89 / SL 143 / EXP 7)
- 最新: ARCSOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,286.66** / 初期 $100.00 (+1186.66%)
- 確定: 6299件 (Win 1846 / Loss 2018 / Flat 2435) / skip 6973件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,286.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.10** / 初期 $100.00 (+174.10%)
- 確定: 3673件 (Win 1023 / Loss 871 / Flat 1779) / skip 6449件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0244 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4869件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000156 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-15T01:26:09.864158+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=81543.5
- Funnel: target 1085 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +16.16% | $4,089,588.98 |
| NIL/USDT:USDT | +14.99% | $11,419,921.24 |
| ARCSOL/USDT:USDT | +14.74% | $1,723,781.16 |
| WAL/USDT:USDT | +10.31% | $14,131,074.44 |
| SOXS/USDT:USDT | +7.65% | $68,121,795.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WAL/USDT:USDT | below_1h_threshold | +3.46% | +3.56% |
| AVA/USDT:USDT | below_1h_threshold | +1.13% | +1.23% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.04% | +1.14% |
| PYTH/USDT:USDT | below_1h_threshold | +0.74% | +0.84% |
| DEEP/USDT:USDT | below_1h_threshold | +0.72% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
